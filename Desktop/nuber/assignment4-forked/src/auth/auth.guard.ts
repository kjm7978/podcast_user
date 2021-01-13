import { UsersService } from './../users/users.service';
import { JwtService } from './../jwt/jwt.service';
import { AllowedRoles } from './role.decorator';
import { GqlExecutionContext } from '@nestjs/graphql';
import { CanActivate, ExecutionContext, Injectable } from "@nestjs/common";
import { Reflector } from '@nestjs/core';

@Injectable()
export class AuthGuard implements CanActivate{
    constructor(
        private readonly refelctor : Reflector,
        private readonly jwtService : JwtService,
        private readonly userService : UsersService,
        ){}
    async canActivate(context : ExecutionContext){
        const roles = this.refelctor.get<AllowedRoles>('roles',context.getHandler(),)
        if(!roles){
            return true;
        }
        const gqlContext = GqlExecutionContext.create(context).getContext()
        const token = gqlContext.token;
        const decoded = this.jwtService.verify(token.toString())
        if(token){
            if(typeof decoded === "object" && decoded.hasOwnProperty('id')){
                const user = await this.userService.findById(decoded['id'])
                if(!user){
                    return false;
                }
                gqlContext['user'] = user;
                if(roles.includes("Any")){
                    return true;
                }
                return true;
                //return roles.includes(user.role);
            }else{
                return false;
            }
        }else{
            return false;
        }
    }
}
