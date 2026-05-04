# ZDI-22-951: Foxit PDF Reader Doc Object color Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-951
- **ZDI-CAN:** ZDI-CAN-17474
- **Date:** 2022-07-07
- **CVE:** CVE-2022-34874
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Foxit
- **Affected Products:** PDF Reader
- **Credit:** Suyue Guo and Wei You from Renmin University of China
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-951/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Foxit PDF Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of Doc objects. By performing actions in JavaScript, an attacker can trigger a read past the end of an allocated object. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxit.com/support/security-bulletins.html

## Disclosure Timeline

- 2022-06-14 - Vulnerability reported to vendor
- 2022-07-07 - Coordinated public release of advisory
