# Database Design

## Database Technology

MongoDB

## Collections

- users
- listings
- bookings
- reviews
- payments
- messages
- notifications
- wishlists
- amenities

## Relationships

- User -> Listings
- Listing -> Reviews
- Booking -> User
- Booking -> Listing
- User -> Wishlist

## Indexes

- email
- listingId
- hostId
- city
- price
- createdAt
- bookingDate

## Validation Rules

- Email format
- Password length (e.g., minimum of 8 characters)
- Unique username
- Price > 0
- Booking dates valid (start date before end date, within a reasonable timeframe)
- Rating between 1-5

## Mongoose Models

- User
- Listing
- Booking
- Review
- Payment
- Message
- Notification
- Wishlist
- Amenity

## API Dependencies

- Create Listing -> Listings
- Book Property -> Users + Listings + Bookings
- Leave Review -> Reviews + Users + Listings
- Secure Payment Gateway Integration -> Payments
- Community Features (e.g., Forums and Events) -> Messages, Notifications, Wishlists

