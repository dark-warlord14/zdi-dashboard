# ZDI-15-040: Schneider Electric SoMove Lite IsObjectModel RemoveParameter Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-040
- **ZDI-CAN:** ZDI-CAN-2478
- **Date:** 2015-02-10
- **CVE:** CVE-2014-9200
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Schneider Electric
- **Affected Products:** SoMove Lite
- **Credit:** Ariele Caltabiano (kimiya)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-040/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Schneider Electric SoMove Lite. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the IsObjectModel.ModelObject.1 ActiveX control in isObjectModel.dll. The control does not check the length of an attacker-supplied string in the RemoveParameter method before copying it into a fixed length buffer on the stack. This allows an attacker to execute arbitrary code in the context of the browser process.

## Additional Details

Schneider Electric has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-15-027-02

## Disclosure Timeline

- 2014-08-13 - Vulnerability reported to vendor
- 2015-02-10 - Coordinated public release of advisory
