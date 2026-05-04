# ZDI-25-462: (0Day) Marvell QConvergeConsole decryptFile Directory Traversal Arbitrary File Write Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-462
- **ZDI-CAN:** ZDI-CAN-24979
- **Date:** 2025-06-27
- **CVE:** CVE-2025-6806
- **CVSS:** 8.2
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:H
- **Affected Vendors:** Marvell
- **Affected Products:** QConvergeConsole
- **Credit:** Andrea Micalizzi aka rgod (@rgod777)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-462/
## Vulnerability Details

This vulnerability allows remote attackers to create arbitrary files on affected installations of Marvell QConvergeConsole. Authentication is not required to exploit this vulnerability. The specific flaw exists within the implementation of the decryptFile method. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to write files in the context of SYSTEM.

## Additional Details

09/19/24 – ZDI submitted the report to the vendor 09/23/24 – the vendor acknowledged the receipt of the report 10/09/24 – the vendor communicated that the product was out of support --Mitigation: The vendor no longer supports or recommends this tool. The product has entered End of Life (EOL) and End of Support (EOS) status after v. 5.5.0.85 was released in January 2022

## Disclosure Timeline

- 2024-09-19 - Vulnerability reported to vendor
- 2025-06-27 - Coordinated public release of advisory
- 2025-06-27 - Advisory Updated
