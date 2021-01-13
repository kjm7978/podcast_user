import { AuthGuard } from './../auth/auth.guard';
import { EditProfileOutput, EditProfileInput } from './dtos/edit-profile.dto';
import { UserProfileInput, UserProfileOutput } from './dtos/user-profile.dto';
import { AuthUser } from './../auth/auth-user.decorator';
import { LoginOutput, LoginInput } from './dtos/login.dto';
import { CreateAccountOutput, CreateAccountInput } from './dtos/create-account.dto';
import { UsersService } from './users.service';
import { Args, Mutation, Resolver, Query, Context } from "@nestjs/graphql";
import { User } from "./entities/user.entity";
import { UseGuards } from '@nestjs/common';


@Resolver(of=>User)
export class UsersResolver{
    constructor(
        private readonly userService : UsersService
    ){}

    @Mutation(returns=>CreateAccountOutput)
    createAccount(@Args("input") createAccountInput:CreateAccountInput):Promise<CreateAccountOutput>{
        return this.userService.createAccount(createAccountInput)
    }


    @Mutation(returns=>LoginOutput)
    login(@Args("input") loginInput: LoginInput):Promise<LoginOutput>{
            return this.userService.login(loginInput)
    }


    @Query(returns => User)
    @UseGuards(AuthGuard)
    me(@AuthUser() authUser : User){
        return authUser;
    }


    @UseGuards(AuthGuard)
    @Query(returns=>UserProfileOutput)
    async seeProfile(
        @Args() userProfileInput:UserProfileInput):Promise<UserProfileOutput>{
        try{
            const user = await this.userService.findById(userProfileInput.userId)
            if(!user){
                throw Error();
            }
            return { ok: true, user,}
        }catch(e){
            return {error : "User Not Found", ok:false}
        }
    }
    
    @UseGuards(AuthGuard)
    @Mutation(returns=>EditProfileOutput)
    async editProfile(
        @AuthUser() authUser : User, @Args("input") editProfileInput:EditProfileInput):Promise<EditProfileOutput>{
        
        return this.userService.editProfile(authUser.id,editProfileInput) 
    }


}