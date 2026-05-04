# ZDI-11-320: GE Proficy Historian ihDataArchiver.exe Trusted Header Size Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-320
- **ZDI-CAN:** ZDI-CAN-1233
- **Date:** 2011-11-07
- **CVE:** CVE-2011-1918
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** GE
- **Affected Products:** Proficy Historian ihDataArchiver
- **Credit:** Luigi Auriemma
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-320/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of GE Proficy Historian. Authentication is not required to exploit this vulnerability. The specific flaw exists within the ihDataArchiver.exe process which listens by default on TCP port 14000. The code within this module trusts a value supplied over the network and uses it as a length when copying user-supplied data to a stack buffer. By providing a large enough value, this buffer can be overflowed leading to arbitrary code execution under the context of the user running the service.

## Additional Details

GE has issued an update to correct this vulnerability. More details can be found at: http://support.ge-ip.com/support/index?page=kbchannel&id=S:KB14493

## Disclosure Timeline

- 2011-06-02 - Vulnerability reported to vendor
- 2011-11-07 - Coordinated public release of advisory
