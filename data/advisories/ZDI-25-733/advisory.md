# ZDI-25-733: (0Day) Marvell QConvergeConsole compressConfigFiles Directory Traversal Information Disclosure and Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-733
- **ZDI-CAN:** ZDI-CAN-24915
- **Date:** 2025-07-31
- **CVE:** CVE-2025-8426
- **CVSS:** 9.4
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:L/A:H
- **Affected Vendors:** Marvell
- **Affected Products:** QConvergeConsole
- **Credit:** Andrea Micalizzi aka rgod (@rgod777)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-733/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information or to create a denial-of-service condition on affected installations of Marvell QConvergeConsole. Authentication is not required to exploit this vulnerability. The specific flaw exists within the implementation of the compressConfigFiles method. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose sensitive information or to create a denial-of-service condition on the system.

## Additional Details

06/05/24 – ZDI submitted the report to the vendor 10/16/24 – the vendor communicated that the product was out of support --Mitigation: The vendor no longer supports or recommends this tool. The product has entered End of Life (EOL) and End of Support (EOS) status after v. 5.5.0.85 was released in January 2022

## Disclosure Timeline

- 2025-06-05 - Vulnerability reported to vendor
- 2025-07-31 - Coordinated public release of advisory
- 2025-07-31 - Advisory Updated
