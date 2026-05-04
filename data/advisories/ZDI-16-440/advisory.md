# ZDI-16-440: Schneider Electric SoMachine HVAC AxEditGrid ActiveX Control SetDataIntf Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-440
- **ZDI-CAN:** ZDI-CAN-3581
- **Date:** 2016-07-20
- **CVE:** CVE-2016-4529
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Schneider Electric
- **Affected Products:** SoMachine HVAC
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-440/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Schneider Electric SoMachine HVAC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the SetDataIntf method of the AxEditGrid control. The control has an untrusted pointer dereference vulnerability because it blindly calls an attacker-supplied memory address. A remote attacker can leverage this vulnerability to execute arbitrary code under the context of the process.

## Additional Details

Schneider Electric has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-16-196-03

## Disclosure Timeline

- 2016-02-18 - Vulnerability reported to vendor
- 2016-07-20 - Coordinated public release of advisory
