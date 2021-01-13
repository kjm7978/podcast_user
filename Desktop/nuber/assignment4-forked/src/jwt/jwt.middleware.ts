import { UsersService } from './../users/users.service';
import { JwtService } from './jwt.service';
import { Injectable, NestMiddleware } from "@nestjs/common";
import { NextFunction ,Request, Response} from "express";


@Injectable()
export class JwtMiddleware implements NestMiddleware{
    constructor(
        private readonly jwtService:JwtService,
        private readonly userService:UsersService,
        ){}
    async use(req:Request, res: Response, next: NextFunction){
        if("x-jwt" in req.headers){
            const token  = req.headers['x-jwt'];
           // console.log(token)
           try{
                const decoded = this.jwtService.verify(token.toString());
           
                if(typeof decoded === "object" && decoded.hasOwnProperty('id')){
         
                
                    const user = await this.userService.findById(decoded['id'])
                    req['user'] = user;
                    console.log(user)
                }
            }catch(e){
                    console.log(e)
            }
        }
        console.log(req.headers)
        next();
    }
    
}


/*export function jwtMiddleware(req:Request, res: Response, next: NextFunction){
    console.log(req.headers)
    next()
}*/