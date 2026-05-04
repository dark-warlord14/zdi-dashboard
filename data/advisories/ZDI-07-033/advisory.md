# ZDI-07-033: Samba lsa_io_trans_names Heap Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-07-033
- **ZDI-CAN:** ZDI-CAN-197
- **Date:** 2007-07-11
- **CVE:** CVE-2007-2446
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Samba
- **Affected Products:** 3.0.x
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-033/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Samba. User interaction is not required to exploit this vulnerability. The specific flaw exists in the parsing of RPC requests to the LSA RPC interface. When parsing a request to LsarLookupSids/LsarLookupSids2, heap allocation is calculated based on user input. By specifying invalid values, heap blocks can be overwritten leading to remote code execution.

## Additional Details

Samba has issued an update to correct this vulnerability. More details can be found at: http://us1.samba.org/samba/security/CVE-2007-2446.html

## Disclosure Timeline

- 2007-05-04 - Vulnerability reported to vendor
- 2007-07-11 - Coordinated public release of advisory
