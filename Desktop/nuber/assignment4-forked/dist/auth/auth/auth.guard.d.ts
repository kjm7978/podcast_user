import { UsersService } from './../users/users.service';
import { JwtService } from './../jwt/jwt.service';
import { CanActivate, ExecutionContext } from "@nestjs/common";
import { Reflector } from '@nestjs/core';
export declare class AuthGuard implements CanActivate {
    private readonly refelctor;
    private readonly jwtService;
    private readonly userService;
    constructor(refelctor: Reflector, jwtService: JwtService, userService: UsersService);
    canActivate(context: ExecutionContext): Promise<any>;
}
