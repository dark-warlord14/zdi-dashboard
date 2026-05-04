# ZDI-25-466: (0Day) Marvell QConvergeConsole readNICParametersFromFile Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-466
- **ZDI-CAN:** ZDI-CAN-25218
- **Date:** 2025-06-27
- **CVE:** CVE-2025-6809
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Marvell
- **Affected Products:** QConvergeConsole
- **Credit:** kimiya
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-466/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Marvell QConvergeConsole. Authentication is not required to exploit this vulnerability. The specific flaw exists within the implementation of the readNICParametersFromFile method. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

10/15/24 – ZDI submitted the report to the vendor 10/16/24 – the vendor communicated that the product was out of support --Mitigation: The vendor no longer supports or recommends this tool. The product has entered End of Life (EOL) and End of Support (EOS) status after v. 5.5.0.85 was released in January 2022

## Disclosure Timeline

- 2024-10-15 - Vulnerability reported to vendor
- 2025-06-27 - Coordinated public release of advisory
- 2025-06-27 - Advisory Updated
