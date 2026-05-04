# ZDI-16-164: Dell SonicWALL GMS Virtual Appliance Multiple Remote Code Execution Vulnerabilities

## Metadata

- **ZDI ID:** ZDI-16-164
- **ZDI-CAN:** ZDI-CAN-3037
- **Date:** 2016-02-10
- **CVE:** CVE-2016-2396
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:S/C:C/I:C/A:C
- **Affected Vendors:** SonicWALL
- **Affected Products:** GMS Virtual Appliance
- **Credit:** kernelsmith - Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-164/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Dell SonicWALL GMS Virtual Appliance. Authentication is required to exploit this vulnerability. The specific flaw exists within the GMS ViewPoint (GMSVP) web application. The issue lies in the handling of configuration input due to a failure to safely sanitize user data before executing a command. An attacker could leverage this vulnerability to execute code with root privileges on the underlying operating system.

## Additional Details

SonicWALL has issued an update to correct this vulnerability. More details can be found at: https://www.mysonicwall.com/firmware/downloadcenter.aspx Hotfix 168056

## Disclosure Timeline

- 2015-07-09 - Vulnerability reported to vendor
- 2016-02-10 - Coordinated public release of advisory
