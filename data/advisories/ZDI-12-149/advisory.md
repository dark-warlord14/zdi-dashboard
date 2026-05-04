# ZDI-12-149: Cisco AnyConnect VPN Client Verification Bypass Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-149
- **ZDI-CAN:** ZDI-CAN-1412
- **Date:** 2012-08-22
- **CVE:** CVE-2012-2494
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Cisco
- **Affected Products:** AnyConnect VPN Client
- **Credit:** gwslabs.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-149/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Cisco AnyConnect VPN Client. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists because the VPN AnyConnect helper program does not check the version number of the vpndownloader.exe program it downloads. As such it is possible to forcefully install an older version of the vpndownloader.exe that is vulnerable to previously patched issues.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: http://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20120620-ac

## Disclosure Timeline

- 2011-11-22 - Vulnerability reported to vendor
- 2012-08-22 - Coordinated public release of advisory
