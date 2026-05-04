# ZDI-23-445: Schneider Electric APC Easy UPS Online getMacAddressByIP Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-445
- **ZDI-CAN:** ZDI-CAN-19269
- **Date:** 2023-04-14
- **CVE:** CVE-2023-29412
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Schneider Electric
- **Affected Products:** APC Easy UPS Online
- **Credit:** Esjay (@esj4y)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-445/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Schneider Electric APC Easy UPS Online. Authentication is not required to exploit this vulnerability. The specific flaw exists within the getMacAddressByIP function. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Schneider Electric has issued an update to correct this vulnerability. More details can be found at: https://download.schneider-electric.com/files?p_Doc_Ref=SEVD-2023-101-04&p_enDocType=Security+and+Safety+Notice&p_File_Name=SEVD-2023-101-04.pdf

## Disclosure Timeline

- 2022-11-30 - Vulnerability reported to vendor
- 2023-04-14 - Coordinated public release of advisory
