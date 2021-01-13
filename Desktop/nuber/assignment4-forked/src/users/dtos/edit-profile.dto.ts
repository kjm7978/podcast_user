import { CoreOutput } from './../../podcast/dtos/output.dto';
import { User } from './../entities/user.entity';
import { InputType, ObjectType, PartialType, PickType } from '@nestjs/graphql';


@ObjectType()
export class EditProfileOutput extends CoreOutput{
    
}

@InputType()
export class EditProfileInput extends PartialType(
    PickType(User, ["email",'password','role']),
){}