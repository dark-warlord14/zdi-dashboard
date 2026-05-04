# ZDI-13-201: Hewlett-Packard Network Node Manager I pmd.exe Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-201
- **ZDI-CAN:** ZDI-CAN-1566
- **Date:** 2013-08-13
- **CVE:** CVE-2013-2351
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** iNode Management Center
- **Credit:** e6af8de8b1d4b2b6d5ba2610cbf9cd38
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-201/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of HP Network Node Manager i. Authentication is not required to exploit this vulnerability. The specific flaw exists within pmd.exe, which listens by default on TCP port 162. By sending a specially crafted packet to the process, an attacker can provide a size to allocate an undersized buffer which will later be used for a memcpy. This vulnerability will cause a corruption of heap memory and allow for an attacker to execute code under the context of the process.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hp.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c03747342

## Disclosure Timeline

- 2012-11-19 - Vulnerability reported to vendor
- 2013-08-13 - Coordinated public release of advisory
