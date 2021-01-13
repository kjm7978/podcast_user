import { EditProfileInput, EditProfileOutput } from './dtos/edit-profile.dto';
import { JwtService } from './../jwt/jwt.service';
import { LoginInput, LoginOutput } from './dtos/login.dto';
import { CreateAccountInput, CreateAccountOutput } from './dtos/create-account.dto';
import { Injectable } from "@nestjs/common";
import { InjectRepository } from "@nestjs/typeorm";
import { Repository } from "typeorm";
import { User } from "./entities/user.entity";
import * as jwt from 'jsonwebtoken';


@Injectable()
export class UsersService {
    constructor( 
        @InjectRepository(User)
        private readonly users : Repository<User>,
        private readonly jwtService : JwtService,
    ){}

    async createAccount({email,password,role}:CreateAccountInput):Promise<CreateAccountOutput>{
        try{
            const exists = await this.users.findOne({email})
            if(exists){
                return {ok:false, error : "There is a user with that email already"}
            }
            await this.users.save(this.users.create({email,password,role}))
            return{ok:true, }
        }catch{
            return{ok:false, error : "Couldn't create account"}
        }
    }

    async login({email,password}:LoginInput):Promise<LoginOutput>{
        try{
            const user = await this.users.findOne({email})
            if(!user){
                return{ok:false, error:"User not found"}
            }
            const passwordCorrect = await user.checkPassword(password)
            if(!passwordCorrect){
                return {ok:false,error:"Wrong password!"}
            }
           const token = this.jwtService.sign(user.id)
           return{ok:true, token }
        }catch{
            return{ok:false, error:"Couldn't login"}
        }
    }


    async findById(id:number):Promise<User>{
        return this.users.findOneOrFail({id});
    }
    
    async editProfile(userId:number, {email, password}:EditProfileInput ):Promise<EditProfileOutput>{
        try{
            const user = await this.users.findOne(userId);
            if(email){
                user.email = email
            }
            if(password){
                user.password = password
            }
            this.users.save(user)
            return{ ok:true, error:`${userId} is updated!`}
        }catch{
            return {ok:false, error: "Couldn't edit profile"}
        }
        
    }

}