# ZDI-20-223: Symantec Endpoint Protection Manager secars Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-223
- **ZDI-CAN:** ZDI-CAN-9535
- **Date:** 2020-02-11
- **CVE:** CVE-2020-5829
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N
- **Affected Vendors:** Symantec
- **Affected Products:** Endpoint Protection
- **Credit:** KPC
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-223/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Symantec Endpoint Protection Manager. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the secars.dll module. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the semwebsrv user.

## Additional Details

Symantec has issued an update to correct this vulnerability. More details can be found at: https://support.symantec.com/us/en/article.SYMSA1505.html

## Disclosure Timeline

- 2019-10-22 - Vulnerability reported to vendor
- 2020-02-11 - Coordinated public release of advisory
