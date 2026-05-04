# ZDI-12-017: Oracle Outside In OOXML Relationship Tag Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-017
- **ZDI-CAN:** ZDI-CAN-1306
- **Date:** 2012-01-20
- **CVE:** N/A
- **CVSS:** 9.7
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:P
- **Affected Vendors:** Oracle
- **Affected Products:** Outside In
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-017/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Outside In. Authentication is not required to exploit this vulnerability. The flaw exists within the sccfut.dll component which is used by multiple vendors, most notably the Novell Groupwise E-Mail Client. When opening the OOXML formatted mail attachment for preview the process copies the target of a Relationship tag to a local stack buffer. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of SYSTEM.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/cpujan2012-366304.html

## Disclosure Timeline

- 2011-11-02 - Vulnerability reported to vendor
- 2012-01-20 - Coordinated public release of advisory
