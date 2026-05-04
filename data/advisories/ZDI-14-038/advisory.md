# ZDI-14-038: Oracle Java TrueType LookupCount Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-038
- **ZDI-CAN:** ZDI-CAN-2020
- **Date:** 2014-04-03
- **CVE:** CVE-2013-5907
- **CVSS:** 9.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** Java Runtime
- **Credit:** John Leitch
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-038/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Java. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of TrueType fonts. The issue lies in the handling of TTF files with an overly large LookupCount. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the process.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/cpujan2014-1972949.html

## Disclosure Timeline

- 2014-02-07 - Vulnerability reported to vendor
- 2014-04-03 - Coordinated public release of advisory
