# ZDI-22-773: Foxit PDF Reader Doc Object Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-773
- **ZDI-CAN:** ZDI-CAN-16778
- **Date:** 2022-05-12
- **CVE:** CVE-2022-28682
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Foxit
- **Affected Products:** PDF Reader
- **Credit:** Suyue Guo and Wei You from Renmin University of China
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-773/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Foxit PDF Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of Doc objects. By performing actions in JavaScript, an attacker can trigger a read past the end of an allocated object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxit.com/support/security-bulletins.html

## Disclosure Timeline

- 2022-03-30 - Vulnerability reported to vendor
- 2022-05-12 - Coordinated public release of advisory
