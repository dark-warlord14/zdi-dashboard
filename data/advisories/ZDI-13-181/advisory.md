# ZDI-13-181: GE Proficy CIMPLICITY CimWebServer Broadcase/Init Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-181
- **ZDI-CAN:** ZDI-CAN-1624
- **Date:** 2013-07-26
- **CVE:** CVE-2013-2785
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** GE
- **Affected Products:** Proficy CIMPLICITY
- **Credit:** ZombiE and amisto0x07
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-181/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of GE Proficy CIMPLICITY. Authentication is not required to exploit this vulnerability. The specific flaw exists within the CimWebServer component. This component performs insufficient bounds checking on user-supplied data passed in the szOptions field which results in stack corruption. An attacker can leverage this situation to execute code under the context of the process.

## Additional Details

GE has issued an update to correct this vulnerability. More details can be found at: http://support.ge-ip.com/support/index?page=kbchannel&id=KB15602

## Disclosure Timeline

- 2013-02-22 - Vulnerability reported to vendor
- 2013-07-26 - Coordinated public release of advisory
