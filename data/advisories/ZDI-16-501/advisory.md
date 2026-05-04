# ZDI-16-501: Google Chrome StylePropertySerializer Type Confusion Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-501
- **ZDI-CAN:** ZDI-CAN-3840
- **Date:** 2016-09-01
- **CVE:** CVE-2016-5161
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Google
- **Affected Products:** Chrome
- **Credit:** 62600BCA031B9EB5CB4A74ADDDD6771E
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-501/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Google Chrome. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the StylePropertySerializer class. By manipulating a document's elements an attacker can trigger a type confusion condition. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Google has issued an update to correct this vulnerability. More details can be found at: http://googlechromereleases.blogspot.com/2016/08/stable-channel-update-for-desktop_31.html

## Disclosure Timeline

- 2016-06-22 - Vulnerability reported to vendor
- 2016-09-01 - Coordinated public release of advisory
