# ZDI-14-242: Advantech WebAccess dvs.ocx SetParameter Stack Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-242
- **ZDI-CAN:** ZDI-CAN-2043
- **Date:** 2014-07-18
- **CVE:** CVE-2014-2364
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Advantech
- **Affected Products:** Advantech WebAccess
- **Credit:** Tom Gallagher
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-242/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Advantech WebAccess. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the DVC.DvcCtrl ActiveX Control in dvs.ocx. The control does not check the length of an attacker-supplied string in the SetParameter method before copying it into a fixed length buffer on the stack. This allows an attacker to execute arbitrary code in the context of the browser process.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: http://ics-cert.us-cert.gov/advisories/ICSA-14-198-02

## Disclosure Timeline

- 2014-04-23 - Vulnerability reported to vendor
- 2014-07-18 - Coordinated public release of advisory
