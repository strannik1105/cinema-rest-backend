async def get_available_cook(db_session, intersection_books, staff_repository):
    staffs = await staff_repository.get_all(db_session)
    if staffs is None or len(staffs) == 0:
        return None
    staffs_dict = {staff.sid: (0, staff) for staff in staffs}

    for booking in intersection_books:
        staffs_dict[booking.cook_sid] = (
            staffs_dict[booking.cook_sid][0] + 1,
            staffs_dict[booking.cook_sid][1],
        )

    available_staffs = [v[1] for k, v in staffs_dict.items() if v[0] < 2]
    if len(available_staffs) > 0:
        return available_staffs[0]
    else:
        return None


async def get_available_waiter(db_session, intersection_books, staff_repository):
    staffs = await staff_repository.get_all(db_session)
    if staffs is None or len(staffs) == 0:
        return None
    staffs_dict = {staff.sid: (0, staff) for staff in staffs}

    for booking in intersection_books:
        staffs_dict[booking.waiter_sid] = (
            staffs_dict[booking.waiter_sid][0] + 1,
            staffs_dict[booking.waiter_sid][1],
        )

    available_staffs = [v[1] for k, v in staffs_dict.items() if v[0] < 2]
    if len(available_staffs) > 0:
        return available_staffs[0]
    else:
        return None
