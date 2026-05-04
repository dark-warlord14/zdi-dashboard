# ZDI-23-1020: Apple Safari PDF Plugin Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1020
- **ZDI-CAN:** ZDI-CAN-19331
- **Date:** 2023-08-04
- **CVE:** CVE-2023-32358
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1020/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the WebKit PDF plugin. The issue results from the lack of proper validation of user-supplied data, which can result in a type confusion condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-ca/HT213670

## Disclosure Timeline

- 2022-11-21 - Vulnerability reported to vendor
- 2023-08-04 - Coordinated public release of advisory
