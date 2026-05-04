# ZDI-19-157: Bitdefender SafePay exec Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-157
- **ZDI-CAN:** ZDI-CAN-7234
- **Date:** 2019-01-29
- **CVE:** CVE-2019-6736
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Bitdefender
- **Affected Products:** SafePay
- **Credit:** Juho Nurminen
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-157/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Bitdefender SafePay. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of tiscript. When processing the System.Exec method the application does not properly validate a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

This issue was resolved with 23.0.11.44.

## Disclosure Timeline

- 2018-09-11 - Vulnerability reported to vendor
- 2019-01-29 - Coordinated public release of advisory
