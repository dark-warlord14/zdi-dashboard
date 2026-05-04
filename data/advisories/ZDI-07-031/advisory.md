# ZDI-07-031: Samba smb_io_notify_option_type_data Heap Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-07-031
- **ZDI-CAN:** ZDI-CAN-193
- **Date:** 2007-07-11
- **CVE:** CVE-2007-2446
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Samba
- **Affected Products:** 3.0.x
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-031/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Samba. User interaction is not required to exploit this vulnerability. The specific flaw exists in the parsing of RPC requests to the SPOOLSS RPC interface. When parsing a request to RFNPCNEX, heap allocation is calculated based on user input. By specifying invalid values, heap blocks can be overwritten leading to remote code execution.

## Additional Details

Samba has issued an update to correct this vulnerability. More details can be found at: http://us1.samba.org/samba/security/CVE-2007-2446.html

## Disclosure Timeline

- 2007-04-25 - Vulnerability reported to vendor
- 2007-07-11 - Coordinated public release of advisory
