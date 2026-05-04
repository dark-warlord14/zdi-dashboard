# ZDI-18-1078: Cisco WebEx Network Recording Player NMVC RtpConfig Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1078
- **ZDI-CAN:** ZDI-CAN-6254
- **Date:** 2018-09-21
- **CVE:** CVE-2018-15421
- **CVSS:** 5.1
- **CVSS Vector:** AV:N/AC:H/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Cisco
- **Affected Products:** WebEx
- **Credit:** Ziad Badawi
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1078/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Cisco WebEx Network Recording Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the NMVC.DLL module. When parsing an ARF file, the process does not properly validate the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20180919-webex

## Disclosure Timeline

- 2018-05-24 - Vulnerability reported to vendor
- 2018-09-21 - Coordinated public release of advisory
- 2018-09-21 - Advisory Updated
