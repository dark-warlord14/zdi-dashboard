# ZDI-15-621: Lepide Active Directory Self Service Arbitrary User Password Change Domain Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-621
- **ZDI-CAN:** ZDI-CAN-3001
- **Date:** 2015-12-08
- **CVE:** CVE-2015-8570
- **CVSS:** 7.4
- **CVSS Vector:** AV:A/AC:M/Au:S/C:C/I:C/A:C
- **Affected Vendors:** Lepide
- **Affected Products:** Active Directory Self Service
- **Credit:** Alain Homewood
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-621/
## Vulnerability Details

This vulnerability allows domain users to reset arbitrary account passwords on vulnerable installations of Lepide Active Directory Self Service. No user interaction is required to exploit this vulnerability. The specific flaw exists within processing of the password reset functionality of Active Directory Self Service. A user should only be able to change the password of other users who have explicitly delegated that power to him. By crafting request packets to the Lepide web service, a domain user can change the password of any user in the Active Directory domain. A malicious user can use this to appropriate the account of a Domain Administrator.

## Additional Details

Lepide has issued an update to correct this vulnerability. More details can be found at: http://www.lepide.com/active-directory-self-service/

## Disclosure Timeline

- 2015-08-20 - Vulnerability reported to vendor
- 2015-12-08 - Coordinated public release of advisory
