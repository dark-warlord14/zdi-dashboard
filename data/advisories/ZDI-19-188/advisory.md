# ZDI-19-188: Microsoft HID Driver Numeric Truncation Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-188
- **ZDI-CAN:** ZDI-CAN-7379
- **Date:** 2019-02-12
- **CVE:** CVE-2019-0600
- **CVSS:** 7.1
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Lucas Leong (@_wmliang_)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-188/
## Vulnerability Details

This vulnerability allows attackers to disclose sensitive information on vulnerable installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists in the hidparse.sys driver, within the function HidPGetSpecificButtonCaps. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges in the context of the kernel.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-0600

## Disclosure Timeline

- 2018-10-18 - Vulnerability reported to vendor
- 2019-02-12 - Coordinated public release of advisory
