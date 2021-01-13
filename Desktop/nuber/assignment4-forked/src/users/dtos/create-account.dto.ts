import { IsString } from 'class-validator';
import { CoreOutput } from './../../podcast/dtos/output.dto';
import { InputType, PickType, ObjectType, Field } from '@nestjs/graphql';
import { User } from '../entities/user.entity';


@InputType()
export class CreateAccountInput extends PickType(User,[
    "email",
    "password",
    "role",
]){}

@ObjectType()
export class CreateAccountOutput extends CoreOutput{

}