# ZDI-17-323: Microsoft Internet Explorer Enhanced Protected Mode Sandbox Escape Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-323
- **ZDI-CAN:** ZDI-CAN-4285
- **Date:** 2017-05-10
- **CVE:** CVE-2017-0226
- **CVSS:** 4.4
- **CVSS Vector:** AV:L/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Thomas Vanhoutte
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-323/
## Vulnerability Details

This vulnerability allows remote attackers to escape the Enhanced Protected Mode (EPM) sandbox on vulnerable installations of Microsoft Internet Explorer. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists due to the EPM sandbox allowing low-privileged code to perform various operations, such as modifying certain low-integrity parts of the file system and calling specific APIs. Considered individually, these operations do not pose a risk. However, they can be used in combination to produce an unsafe result. An attacker can leverage this in conjunction with other vulnerabilities to execute code under the context of the user at medium integrity.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2017-0226

## Disclosure Timeline

- 2016-12-12 - Vulnerability reported to vendor
- 2017-05-10 - Coordinated public release of advisory
