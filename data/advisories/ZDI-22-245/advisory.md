# ZDI-22-245: (Pwn2Own) Samba fruit_pread Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-245
- **ZDI-CAN:** ZDI-CAN-15833
- **Date:** 2022-02-01
- **CVE:** CVE-2021-44142
- **CVSS:** 5.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N
- **Affected Vendors:** Samba
- **Affected Products:** Samba
- **Credit:** Nguyen Hoang Thach (https://twitter.com/hi_im_d4rkn3ss) and Billy Jheng Bing-Jhong (https://twitter.com/st424204)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-245/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Samba. Authentication is not required to exploit this vulnerability. The specific flaw exists within the fruit_pread method. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of root.

## Additional Details

Samba has issued an update to correct this vulnerability. More details can be found at: https://www.samba.org/samba/security/CVE-2021-44142.html

## Disclosure Timeline

- 2021-12-03 - Vulnerability reported to vendor
- 2022-02-01 - Coordinated public release of advisory
- 2022-02-01 - Advisory Updated
