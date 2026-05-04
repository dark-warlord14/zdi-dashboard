# ZDI-10-072: Cisco Secure Desktop CSDWebInstaller ActiveX Control Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-072
- **ZDI-CAN:** ZDI-CAN-438
- **Date:** 2010-04-14
- **CVE:** CVE-2010-0589
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Cisco
- **Affected Products:** Secure Desktop
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-072/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on systems with vulnerable installations of Cisco Secure Desktop. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists in the Secure Desktop Web Install ActiveX control (705EC6D4-B138-4079-A307-EF13E4889A82). The control fails to properly verify the signature of the downloaded executable being installed. By not verifying the executable a malicious attacker can force the user to download and run any code of their choosing. Successful exploitation leads to full system compromise under the credentials of the currently logged in user.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: http://www.cisco.com/en/US/products/products_security_advisory09186a0080b25d01.shtml

## Disclosure Timeline

- 2009-02-24 - Vulnerability reported to vendor
- 2010-04-14 - Coordinated public release of advisory
