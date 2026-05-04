# ZDI-16-208: IBM Informix nsrd Service Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-208
- **ZDI-CAN:** ZDI-CAN-3457
- **Date:** 2016-03-22
- **CVE:** CVE-2016-0226
- **CVSS:** 6.8
- **CVSS Vector:** AV:L/AC:L/Au:S/C:C/I:C/A:C
- **Affected Vendors:** IBM
- **Affected Products:** Informix
- **Credit:** Steven Seeley of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-208/
## Vulnerability Details

This vulnerability allows local users to execute arbitrary code on vulnerable installations of IBM Informix. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within configuration of the nsrd service. Weak access control allows all authenticated users to modify the binary for this service and thus execute code in the context of SYSTEM.

## Additional Details

IBM has issued an update to correct this vulnerability. More details can be found at: http://www-01.ibm.com/support/docview.wss?rs=630&uid=swg21978598

## Disclosure Timeline

- 2015-12-16 - Vulnerability reported to vendor
- 2016-03-22 - Coordinated public release of advisory
