import { Field, InputType, ObjectType, registerEnumType } from '@nestjs/graphql';
import { CoreEntity } from './../../common/entities/core.entity';
import { BeforeInsert, BeforeUpdate, Column, Entity } from "typeorm";
import * as bcrypt from "bcrypt";
import { InternalServerErrorException } from '@nestjs/common';
import { IsEAN, IsEmail, IsEnum } from 'class-validator';


export enum UserRole {
    host,
    listner,
} 

registerEnumType(UserRole,{name:"UserRole"})
@InputType({isAbstract:true})
@ObjectType()
@Entity()
export class User extends CoreEntity{
    @Column()
    @Field(type=>String)
    @IsEmail()
    email:string;

    @Column()
    @Field(type=>String)
    password:string;

    @Column({type:'simple-enum', enum:UserRole})
    @Field(type=>UserRole)
    @IsEnum(UserRole)
    role:UserRole;


    @BeforeInsert()
    @BeforeUpdate()
    async hashPassword(): Promise<void>{
        try{
            this.password = await bcrypt.hash(this.password,10)
        }catch{
            throw new InternalServerErrorException()
        }
    }

    async checkPassword(aPassword : string):Promise<boolean>{
        try{
            const ok = await bcrypt.compare(aPassword,this.password)
            return ok;
        }catch{
            throw new InternalServerErrorException()
        }
    } 
}