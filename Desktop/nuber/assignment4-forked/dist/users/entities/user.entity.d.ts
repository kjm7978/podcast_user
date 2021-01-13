import { CoreEntity } from './../../common/entities/core.entity';
export declare enum UserRole {
    host = 0,
    listner = 1
}
export declare class User extends CoreEntity {
    email: string;
    password: string;
    role: UserRole;
    hashPassword(): Promise<void>;
    checkPassword(aPassword: string): Promise<boolean>;
}
