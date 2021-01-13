import { UsersService } from './../users/users.service';
import { JwtService } from './jwt.service';
import { NestMiddleware } from "@nestjs/common";
import { NextFunction, Request, Response } from "express";
export declare class JwtMiddleware implements NestMiddleware {
    private readonly jwtService;
    private readonly userService;
    constructor(jwtService: JwtService, userService: UsersService);
    use(req: Request, res: Response, next: NextFunction): Promise<void>;
}
