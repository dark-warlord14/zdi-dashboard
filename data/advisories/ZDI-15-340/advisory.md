# ZDI-15-340: NetIQ Security Solutions for ISeries NetIQExecObject.NetIQExec.1 SafeShellExecute Stack Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-340
- **ZDI-CAN:** ZDI-CAN-2699
- **Date:** 2015-07-14
- **CVE:** CVE-2015-0795
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** NetIQ
- **Affected Products:** Security Solutions for ISeries
- **Credit:** Andrea Micalizzi (rgod)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-340/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of NetIQ Security Solutions for ISeries. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the NetIQExecObject.NetIQExec.1 ActiveX Control. By providing overly long arguments to the SafeShellExecute function, an attacker can overflow fixed size stack buffers and execute arbitrary code in the context of the browser.

## Additional Details

NetIQ has issued an update to correct this vulnerability. More details can be found at: http://www.netiq.com/support/7016656

## Disclosure Timeline

- 2015-01-27 - Vulnerability reported to vendor
- 2015-07-14 - Coordinated public release of advisory
