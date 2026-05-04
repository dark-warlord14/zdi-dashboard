# ZDI-21-342: Samsung Galaxy S20 libimagecodec Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-342
- **ZDI-CAN:** ZDI-CAN-11806
- **Date:** 2021-03-22
- **CVE:** CVE-2021-25346
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Samsung
- **Affected Products:** Galaxy S20
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-342/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Samsung Galaxy S20. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the Quram ImageCodec component. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Samsung has issued an update to correct this vulnerability. More details can be found at: https://security.samsungmobile.com/securityUpdate.smsb

## Disclosure Timeline

- 2020-10-06 - Vulnerability reported to vendor
- 2021-03-22 - Coordinated public release of advisory
