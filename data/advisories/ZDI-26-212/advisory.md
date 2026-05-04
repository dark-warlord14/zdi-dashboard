# ZDI-26-212: Schneider Electric EcoStruxure Data Center Expert Hard-coded Password Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-212
- **ZDI-CAN:** ZDI-CAN-28034
- **Date:** 2026-03-16
- **CVE:** CVE-2025-13957
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Schneider Electric
- **Affected Products:** EcoStruxure Data Center Expert
- **Credit:** hassan ali
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-212/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Schneider Electric EcoStruxure Data Center Expert. Authentication is required to exploit this vulnerability. The specific flaw exists within the postgres service, which listens on TCP port 5432 by default. The issue results from the use of hard-coded credentials. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

Schneider Electric has issued an update to correct this vulnerability. More details can be found at: https://download.schneider-electric.com/files?p_Doc_Ref=SEVD-2026-069-05&p_enDocType=Security+and+Safety+Notice&p_File_Name=SEVD-2026-069-05.pdf

## Disclosure Timeline

- 2026-02-02 - Vulnerability reported to vendor
- 2026-03-16 - Coordinated public release of advisory
- 2026-03-16 - Advisory Updated
