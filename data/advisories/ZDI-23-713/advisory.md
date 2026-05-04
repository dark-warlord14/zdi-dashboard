# ZDI-23-713: Samba SMB1 Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-713
- **ZDI-CAN:** ZDI-CAN-17388
- **Date:** 2023-05-24
- **CVE:** CVE-2022-32742
- **CVSS:** 5.9
- **CVSS Vector:** AV:N/AC:H/PR:L/UI:N/S:U/C:L/I:N/A:H
- **Affected Vendors:** Samba
- **Affected Products:** Samba
- **Credit:** Luca Moro (@johncool__)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-713/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Samba. Authentication is required to exploit this vulnerability, and SMB1 must be enabled on the target. The specific flaw exists within the Samba service, which listens on TCP port 139 by default. A crafted SMB1 command can trigger a read past the end of an allocated buffer. An attacker can leverage this vulnerability to disclose information in the context of the Samba service process or to create a denial-of-service condition on the system.

## Additional Details

Samba has issued an update to correct this vulnerability. More details can be found at: https://www.samba.org/samba/security/CVE-2022-32742.html

## Disclosure Timeline

- 2022-06-01 - Vulnerability reported to vendor
- 2023-05-24 - Coordinated public release of advisory
