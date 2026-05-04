# ZDI-16-682: ThinPrint TPClnt/TPView Heap-based Buffer Overflow Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-682
- **ZDI-CAN:** ZDI-CAN-3783
- **Date:** 2017-06-02
- **CVE:** CVE-2016-7081
- **CVSS:** 6.2
- **CVSS Vector:** AV:L/AC:H/Au:N/C:C/I:C/A:C
- **Affected Vendors:** ThinPrint
- **Affected Products:** ThinPrint
- **Credit:** E0DB6391795D7F629B5077842E649393
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-682/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on vulnerable installations of ThinPrint. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of print requests. The issue lies in the failure to properly validate the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to escalate privileges under the context of the host OS.

## Additional Details

ThinPrint has issued an update to correct this vulnerability. More details can be found at: https://www.vmware.com/security/advisories/VMSA-2016-0014.html

## Disclosure Timeline

- 2016-06-14 - Vulnerability reported to vendor
- 2017-06-02 - Coordinated public release of advisory
