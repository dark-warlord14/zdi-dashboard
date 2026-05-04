# ZDI-15-533: Apple Safari TTF Out-Of-Bounds Access Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-533
- **ZDI-CAN:** ZDI-CAN-3268
- **Date:** 2015-10-21
- **CVE:** CVE-2015-6978
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** Jaanus Kp Clarified Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-533/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of fonts embedded in PDFs. An attacker could leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT205375

## Disclosure Timeline

- 2015-09-03 - Vulnerability reported to vendor
- 2015-10-21 - Coordinated public release of advisory
