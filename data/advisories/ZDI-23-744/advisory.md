# ZDI-23-744: SAP SQL Anywhere Database Server Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-744
- **ZDI-CAN:** ZDI-CAN-17336
- **Date:** 2023-05-31
- **CVE:** CVE-2022-35299
- **CVSS:** 8.1
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** SAP
- **Affected Products:** SQL Anywhere
- **Credit:** Maxim Kutyavin (https://github.com/pwnhacker0x18)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-744/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of SAP SQL Anywhere. Authentication is not required to exploit this vulnerability. The specific flaw exists within the Database Server, which listens on TCP and UDP ports 2638 by default. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the root.

## Additional Details

SAP has issued an update to correct this vulnerability. More details can be found at: https://d.dam.sap.com/a/3Hat4sC/2022%2012%20Patch%20Day%20Blog%20V9.0.pdf?rc=10

## Disclosure Timeline

- 2022-07-19 - Vulnerability reported to vendor
- 2023-05-31 - Coordinated public release of advisory
