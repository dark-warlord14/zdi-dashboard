# ZDI-20-339: (Pwn2Own) TP-Link Archer A7 tmpServer Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-339
- **ZDI-CAN:** ZDI-CAN-9662
- **Date:** 2020-03-25
- **CVE:** CVE-2020-10886
- **CVSS:** 8.1
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** TP-Link
- **Affected Products:** Archer A7
- **Credit:** F-Secure Labs - Mark Barnes, Toby Drew, Max Van Amerongen, and James Loureiro
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-339/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of TP-Link Archer A7 AC1750 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the tmpServer service, which listens on TCP port 20002. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fixed in version A7(US)_V5_200220

## Disclosure Timeline

- 2019-11-19 - Vulnerability reported to vendor
- 2020-03-25 - Coordinated public release of advisory
