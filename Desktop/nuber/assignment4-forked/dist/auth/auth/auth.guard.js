"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
var _a, _b;
Object.defineProperty(exports, "__esModule", { value: true });
exports.AuthGuard = void 0;
const users_service_1 = require("./../users/users.service");
const jwt_service_1 = require("./../jwt/jwt.service");
const graphql_1 = require("@nestjs/graphql");
const common_1 = require("@nestjs/common");
const core_1 = require("@nestjs/core");
let AuthGuard = class AuthGuard {
    constructor(refelctor, jwtService, userService) {
        this.refelctor = refelctor;
        this.jwtService = jwtService;
        this.userService = userService;
    }
    async canActivate(context) {
        const roles = this.refelctor.get('roles', context.getHandler());
        if (!roles) {
            return true;
        }
        const gqlContext = graphql_1.GqlExecutionContext.create(context).getContext();
        const token = gqlContext.token;
        const decoded = this.jwtService.verify(token.toString());
        if (token) {
            if (typeof decoded === "object" && decoded.hasOwnProperty('id')) {
                const user = await this.userService.findById(decoded['id']);
                if (!user) {
                    return false;
                }
                gqlContext['user'] = user;
                if (roles.includes("Any")) {
                    return true;
                }
                return roles.includes(user.role);
            }
            else {
                return false;
            }
        }
        else {
            return false;
        }
    }
};
AuthGuard = __decorate([
    common_1.Injectable(),
    __metadata("design:paramtypes", [core_1.Reflector, typeof (_a = typeof jwt_service_1.JwtService !== "undefined" && jwt_service_1.JwtService) === "function" ? _a : Object, typeof (_b = typeof users_service_1.UsersService !== "undefined" && users_service_1.UsersService) === "function" ? _b : Object])
], AuthGuard);
exports.AuthGuard = AuthGuard;
//# sourceMappingURL=auth.guard.js.map