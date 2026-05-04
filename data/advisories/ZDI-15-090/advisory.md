# ZDI-15-090: Schneider Electric DS-NVs Rvctl.RVControl.1 SetText Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-090
- **ZDI-CAN:** ZDI-CAN-2341
- **Date:** 2015-03-12
- **CVE:** CVE-2015-0982
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Schneider Electric
- **Affected Products:** DS-NVs
- **Credit:** Ariele Caltabiano (kimiya) and Andrea Micalizzi (rgod)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-090/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Schneider Electric DS-NVs. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the Rvctl.RVControl.1 ActiveX Control in rvctl.dll. The control does not check the length of an attacker-supplied string in the SetText method before copying it into a fixed length buffer on the stack. This allows an attacker to execute arbitrary code in the context of the browser process.

## Additional Details

Schneider Electric has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-15-071-01

## Disclosure Timeline

- 2014-08-13 - Vulnerability reported to vendor
- 2015-03-12 - Coordinated public release of advisory
