# ZDI-14-037: IBM Platform Symphony DE Auth-Bypass Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-037
- **ZDI-CAN:** ZDI-CAN-1970
- **Date:** 2014-04-03
- **CVE:** CVE-2013-5400
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** IBM
- **Affected Products:** Platform Symphony DE
- **Credit:** AbdulAziz Hariri HP Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-037/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of IBM Platform Symphony DE. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the SoamGui servlet. The servlet uses a fixed username and password which allows a malicious user to execute commands remotely in the context of the process.

## Additional Details

IBM has issued an update to correct this vulnerability. More details can be found at: http://www-01.ibm.com/support/docview.wss?uid=isg3T1020564

## Disclosure Timeline

- 2013-11-03 - Vulnerability reported to vendor
- 2014-04-03 - Coordinated public release of advisory
