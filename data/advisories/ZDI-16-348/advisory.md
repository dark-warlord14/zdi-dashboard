# ZDI-16-348: Trend Micro InterScan Web Security ManagePatches filename Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-348
- **ZDI-CAN:** ZDI-CAN-3566
- **Date:** 2016-05-20
- **CVE:** N/A
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:S/C:C/I:C/A:C
- **Affected Vendors:** Trend Micro
- **Affected Products:** InterScan Web Security
- **Credit:** k0rpr1t_z0mb1e
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-348/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Trend Micro InterScan Web Security. Authentication is required to exploit this vulnerability. The specific flaw exists within the ManagePatches servlet. The vulnerability is caused by the lack of input validation before passing a remotely supplied string to a system call. By sending a crafted request to a vulnerable system, a remote attacker can exploit this vulnerability to execute arbitrary code in the context of root.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: http://esupport.trendmicro.com/solution/en-US/1114185.aspx

## Disclosure Timeline

- 2016-02-09 - Vulnerability reported to vendor
- 2016-05-20 - Coordinated public release of advisory
