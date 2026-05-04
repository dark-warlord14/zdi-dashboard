# ZDI-20-216: Apple Messages HandwritingProvider Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-216
- **ZDI-CAN:** ZDI-CAN-9383
- **Date:** 2020-02-11
- **CVE:** CVE-2020-3877
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** Apple
- **Affected Products:** Message
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-216/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Apple Messages. User interaction is required to exploit this vulnerability in that the target must open the Messages application. The specific flaw exists within the HandwritingProvider module in the Messages application. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT210919

## Disclosure Timeline

- 2019-10-29 - Vulnerability reported to vendor
- 2020-02-11 - Coordinated public release of advisory
