# ZDI-13-276: Cisco WAAS Mobile Server ReportReceiver CAB Processing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-276
- **ZDI-CAN:** ZDI-CAN-1862
- **Date:** 2013-12-15
- **CVE:** CVE-2013-5554
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Cisco
- **Affected Products:** WAAS Mobile Server
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-276/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of CISCO WAAS Mobile Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of CAB files uploaded through ReportReceiver. By uploading a crafted CAB file, an attacker is able to add a hostile web page to the web server. Using this, an attacker is able to run arbitrary code as either DefaultAppPool or NetworkService, depending on the operating system version.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: http://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20131106-waasm

## Disclosure Timeline

- 2013-06-21 - Vulnerability reported to vendor
- 2013-12-15 - Coordinated public release of advisory
