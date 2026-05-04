# ZDI-15-552: IBM System Networking Switch Center DB Service Remote Elevation of Privilege Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-552
- **ZDI-CAN:** ZDI-CAN-3010
- **Date:** 2015-11-10
- **CVE:** CVE-2015-7819
- **CVSS:** 7.1
- **CVSS Vector:** AV:N/AC:M/Au:N/C:C/I:N/A:N
- **Affected Vendors:** IBM
- **Affected Products:** System Networking Switch Center
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-552/
## Vulnerability Details

This vulnerability allows remote attackers to disclose information on vulnerable installations of IBM System Networking Switch Center. Authentication is not required to exploit this vulnerability. The specific flaw exists within the IBM SNSC DB Service, that listens by default on port 40999. This service allows an unauthenticated user to obtain the account details for the SNSC Administrator, including the password. The password is stored using reversible encryption, and both the key and salt are static. An attacker can use this information to obtain the plaintext password for the SNSC Administrator or any other known account.

## Additional Details

IBM has issued an update to correct this vulnerability. More details can be found at: https://support.lenovo.com/us/en/product_security/len_2015_074

## Disclosure Timeline

- 2015-06-25 - Vulnerability reported to vendor
- 2015-11-10 - Coordinated public release of advisory
